import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID
from . import DS3502Component, ds3502_ns

DEPENDENCIES = ["ds3502"]

CONF_DS3502_ID = "ds3502_id"

DS3502Sensor = ds3502_ns.class_("DS3502Sensor", sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        DS3502Sensor,
        accuracy_decimals=0,
    )
    .extend(
        {
            cv.Required(CONF_DS3502_ID): cv.use_id(DS3502Component),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(cv.polling_component_schema("60s"))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    
    parent = await cg.get_variable(config[CONF_DS3502_ID])
    cg.add(var.set_parent(parent))