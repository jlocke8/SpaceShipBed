/*
This project ultimately is to provide the system needed to run a spaceship control panel.
This code uses an Arduino with I2C I/O expanders in order to read the status of several switch panels 
so it can relay the status updates via USART Serial Port to a master software whch actively 
receives the serial based status updates.  The master software will then initialize scripts or forward
the switch states to act as a virtual joystick/keyboard.

Each spaceship control panel consists of many pushbutton and toggle switches.  Each panel may have
2 to 4 I2C based I/0 Expanders.  The I/O expanders are Microchip P/N: MCP23017
*/

#include <Arduino.h>
#include <Adafruit_MCP23X17.h>

typedef enum
{
  sw = 1

} TopPanelSwitches;

typedef enum
{
  sw1 = 1

} FrontSidePanelSwitches;

typedef enum
{
  A0_IC5_LifeSupport = 1,
  A1_IC5_PowerBank,
  A2_IC5_BoobooJuice,
  A3_IC5_CellsMain,
  A4_IC5_CellsAux,
  A5_IC5_Atootie,
  A6_IC5_FootyToe,
  A7_IC5_Auto1,
  B0_IC5_Reactor1,
  B1_IC5_Pump1,
  B2_IC5_APU1,
  B3_IC5_Reactor2,
  B4_IC5_Pump2,
  B5_IC5_APU2,
  B6_IC5_O2Synth,
  B7_IC5_CO2Scrub

} BackSidePanelSwitches;

//DEFINES
#define MAX_MSG_LEN (100)
#define LED_PIN (13)

//I2C chip address definitions
//MCP23017 only has 3 bits of user configurable addresses from 0-7
//MCP23017 has a 7 bit address 0100XXX in binary or 0x2X with X being 0-7
//MCP23017 IO expander has 16 switches per IC chip
#define I2C_ADDR_TOPPANEL_IC1 (0x20)
#define I2C_ADDR_TOPPANEL_IC2 (0x21)
#define I2C_ADDR_TOPPANEL_IC3 (0x22)
#define I2C_ADDR_FRONTSIDEPANEL_IC1 (0x23)
#define I2C_ADDR_FRONTSIDEPANEL_IC2 (0x24)
#define I2C_ADDR_BACKSIDEPANEL_IC1 (0x25)
#define I2C_ADDR_BACKSIDEPANEL_IC2 (0x26)

#define I2C_SPEED_FAST 400000L
#define I2C_SPEED_SLOW 100000L

const int8_t TOPPANEL_IC1 = 0;
const int8_t TOPPANEL_IC2 = 1;
const int8_t TOPPANEL_IC3 = 2;
const int8_t FRONTSIDEPANEL_IC1 = 3;
const int8_t FRONTSIDEPANEL_IC2 = 4;
const int8_t BACKSIDEPANEL_IC1 = 5;
const int8_t BACKSIDEPANEL_IC2 = 6;
const int8_t NUM_EXPANDERS = 7;
const int8_t ONBOARD_GPIO = 7;

int8_t i = 0;

union buttonStatus_t
{
  uint8_t states8[8][2];
  uint16_t states16[8] = {0};
} buttons;

char message[100];  //send buffer for outgoing serial messages

Adafruit_MCP23X17 mcp[NUM_EXPANDERS];
bool mcpActive[NUM_EXPANDERS];

const char heart_beat[] = "(^_^)\n";
const char cmd_get_status[] = "GSTAT";

//Function prototypes
static uint8_t scanGPIO(Adafruit_MCP23X17 &expander, int chipNumber, buttonStatus_t &buttonStates, char (&statusMessage)[MAX_MSG_LEN]);
template <int N>
static uint8_t readSerial(char (&read_buffer)[N]);

static uint8_t sendStatus(void);


void setup()
{
  // put your setup code here, to run once:

  //setup gpio as inputs
  //pinMode(2, OUTPUT);
  //pinMode(3,INPUT);
  pinMode(LED_PIN, OUTPUT);

  //setup uart
  Serial.begin(230400);
  Serial.setTimeout(200); //set serial wait time for 30 ms
  while (!Serial)
  {
    ; //spin if not setup correctly
  }
  Serial.println("\nSerial Port Connected at baud rate 230400");

  //setup I2C instance, single I2C bus for multiple IO expander chips
  //Wire.begin();
  //Wire.setClock(I2C_SPEED_SLOW);
  //TWBR = 10;
  //Wire.setClock(I2C_SPEED_FAST);
 // Wire.setWireTimeout(3000, true);

  //setup I2C devices
  for (i = 0; i < NUM_EXPANDERS; i++)
  { //if(!mcp[i].begin_I2C(I2C_ADDR_BACKSIDEPANEL_IC1, &Wire))
    if (!mcp[i].begin_I2C((0x20 + i), &Wire))
    {
      mcpActive[i] = false;
      Serial.print("ERROR! Could not initialize GPIO expander Addr:0x2");
      Serial.println(i);
    }
    else
    {
      mcpActive[i] = true;
      Serial.print("Success. Initialized GPIO expander Addr:0x2");
      Serial.println(i);
    }

    delay(10);
  }




  //setup IO expander pinmodes
  //Note: all MCP23017 pin modes defaults to input
  //mcp[5].pinMode(A0_IC5_LifeSupport, INPUT);
}

static uint8_t last = 0;
static uint8_t tick_1ms = 0;
static uint8_t tick_10ms = 0;
static uint8_t tick_100ms = 0;
static uint8_t tick_1sec = 0;
static char command[10];    //read buffer for incoming serial commands

void loop()
{
  // put your main code here, to run repeatedly:
  //Serial.println("\nSerial Port Connected at baud rate 230400");
  delay(1);
  if (tick_1ms++ >= 10)
  {
    tick_1ms = 0;

    if (tick_10ms++ >= 10)
    {
      tick_10ms = 0;
      if (tick_100ms++ >= 10)
      {
        tick_100ms = 0;
        if (tick_1sec++ >= 10)
        {
          tick_1sec = 0;
        }
        else
        { //1second ticks
          //Send serial line heart beat
          Serial.print(heart_beat);
        }
      }
      else
      { //100ms ticks
        //Toggle heartbeat LED
        if (digitalRead(LED_PIN))
        {
          digitalWrite(LED_PIN, LOW);
        }
        else
        {
          digitalWrite(LED_PIN, HIGH);
        }

        // //poll any incoming serial messages from the master
        // if(Serial.available() !=0){
        //   //read serial buffer
        //   k=Serial.available(); //get number of bytes in read buffer (max 128)
  
        //   Serial.readBytesUntil(ch, command, k);  //read bytes into command buffer
        //   command[++k]='\0';  //set last character as null terminator
        //   Serial.print("***INCOMING*** ack command receieved: ");
        //   Serial.print(command);          
        //   //Serial.flush();
        // }
        
        // if(strlen(command)>0){
        //   if(strcmp(command, cmd_get_status)==0){   //commands strings match

        //     //send status of all the buttons to the serial master
        //     Serial.println("STATUS IS THIS");

        //   }
        //   command[0]='\0';    //reset command buffer by setting first character as null terminator        
        // }

        readSerial<sizeof(command)>(command);

      }
    }
    else
    { //10ms ticks
      /*
      //poll status of onboard GPIO
      uint8_t read = 0;
      read = digitalRead(3);
      if(read != buttons.states8[ONBOARD_GPIO][0]){
          //add this button status to queue of changed states
          buttons.states8[ONBOARD_GPIO][0] = read;

          //print
          sprintf(message, "\nButton %d changed state. It is now: %d", 3, read);
          Serial.println(message);  
      }
*/


      
      //poll status of IO expanders
      //compare read to that of stored state

      for (i = 0; i < NUM_EXPANDERS; i++)
      {
        if (mcpActive[i])
          scanGPIO(mcp[i], i, buttons, message);
      }

      //report only status of those that changed state
      if (strlen(message) > 0)
      {
        Serial.println(message);
        message[0] = '\0';
      }
    }
  }
  else
  { // 1ms ticks
  }
}


//Function "readSerial"
//Description:
//polls the serial port for any incoming messages
//if there is a message copy it to the reference buffer 
//then process the buffer to read in and execute any commands
static char ch, k;
template <int N>
uint8_t readSerial(char (&read_buffer)[N]){
        //poll any incoming serial messages from the master
        if(Serial.available() !=0){
          //read serial buffer
          k=Serial.available(); //get number of bytes in read buffer (max 128)
  
          Serial.readBytesUntil(ch, read_buffer, k);  //read bytes into command buffer
          read_buffer[++k]='\0';  //set last character as null terminator
          Serial.print("***INCOMING*** ack command receieved: ");
          Serial.print(read_buffer);          
          //Serial.flush();
        }

        //parse serial message for commands
        if(strlen(read_buffer)>0){
          if(strcmp(read_buffer, cmd_get_status)==0){   //commands strings match

            //send status of all the buttons to the serial master
            Serial.println("STATUS IS THIS");

          }
          read_buffer[0]='\0';    //reset command buffer by setting first character as null terminator        
        }

  return 0;
}


//Function "scanGPIO"
//Description:
//reads pin status's of GPIO expander chips.
//reads 8 pins from port A and then 8 pins of port B
//then compares reading to previous status of button states
//if new state is read, then the updated status is reported to the outgoing status message
uint8_t scanGPIO(Adafruit_MCP23X17 &expander, int chipNumber, buttonStatus_t &buttonStates, char (&statusMessage)[MAX_MSG_LEN])
{
  uint8_t read;

  read = expander.readGPIOA();
  if (read != buttonStates.states8[chipNumber][0])
  {
    buttonStates.states8[chipNumber][0] = read; //update button status
    sprintf(statusMessage + strlen(statusMessage), "#%dA:%x", chipNumber, read);
    //Serial.println(statusMessage);
  }

  read = expander.readGPIOB();
  if (read != buttonStates.states8[chipNumber][1])
  {
    buttonStates.states8[chipNumber][1] = read;
    sprintf(statusMessage + strlen(statusMessage), "#%dB:%x", chipNumber, read);
    //Serial.println(statusMessage);
  }
  return 0;
}