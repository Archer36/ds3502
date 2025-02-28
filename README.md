## External Component DS3502 for ESPHOME 2025.2.1 ->


Copy the folder `ds3502` which is located in `components` to the identical folder at your instance.
Create your YAML and smile again - DS3502 is back and working in ESPHOME :)


> Example YAML:
```
# Include the local components directory
external_components:
  - source: 
      type: local
      path: components

# I2C bus configuration
i2c:
  sda: GPIO6          # Replace with your GPIO configuration
  scl: GPIO7          # Replace with your GPIO configuration
  scan: true
  frequency: 100kHz   # Lower frequency for reliability

# Create the DS3502 base component
ds3502:
  id: my_ds3502
  address: 0x28

# Create the DS3502 output
output:
  - platform: ds3502
    id: fan_output
    ds3502_id: my_ds3502

# Fan component
fan:
  - platform: speed
    output: fan_output
    name: "DS3502 Fan"
    speed_count: 100
```
