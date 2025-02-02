#include <ArduinoJson.h>

// Adjust the capacity based on your JSON document size
const int capacity = JSON_OBJECT_SIZE(10);

void setup() {
  Serial.begin(9600);
  while (!Serial) continue;
}

void loop() {
  // Check if data is available to read
  if (Serial.available()) {
    // Create a buffer for incoming data
    StaticJsonDocument<capacity> doc;
    
    // Read the JSON string from Serial
    String jsonString = Serial.readStringUntil('\n');
    
    // Deserialize the JSON document
    DeserializationError error = deserializeJson(doc, jsonString);

    // Test if parsing succeeds
    if (error) {
      Serial.print("{\"error\":\"deserialize failed: ");
      Serial.print(error.c_str());
      Serial.println("\"}");
      return;
    }

    // Example: Process received JSON data
    const char* command = doc["command"];
    
    // Example: Handle LED control command
    if (strcmp(command, "LED_CONTROL") == 0) {
      const char* state = doc["state"];
      int brightness = doc["brightness"];
      
      // Process the command (example)
      // digitalWrite(LED_PIN, strcmp(state, "ON") == 0 ? HIGH : LOW);
      
      // Send response back
      StaticJsonDocument<capacity> response;
      response["status"] = "success";
      response["command_received"] = command;
      response["state"] = state;
      response["brightness"] = brightness;
      
      // Serialize the response to JSON and send
      serializeJson(response, Serial);
      Serial.println(); // Add newline for Python parsing
    }
  }
}
