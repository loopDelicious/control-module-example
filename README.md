# Module control-lamp-alarm

This module provides the control logic for turning on and off a smart plug connected to a lamp based on computer vision detections.

## Model joyce:control-lamp-alarm:lamp-alarm

Turn on the lights when a person is detected. Turn off the lights 3 minutes after no person is detected.

### Configuration

The following attribute template can be used to configure this model:

```json
{
  "generic": <string>,
  "camera": <string>,
  "vision": <string>
}
```

#### Attributes

The following attributes are available for this model:

| Name      | Type   | Inclusion | Description                                           |
| --------- | ------ | --------- | ----------------------------------------------------- |
| `generic` | string | Required  | Name of the Kasa smart plug component in the Viam app |
| `camera`  | string | Required  | Name of the webcam component in the Viam app          |
| `vision`  | string | Required  | Name of the vision service in the Viam app            |

#### Example Configuration

```json
{
  "generic": "smart-plug",
  "camera": "camera-1",
  "vision": "vision-people-detector"
}
```

### DoCommand

This step is only required during development and testing, not in production. To start your control logic, copy and paste the following command input, and click **Execute**:

```json
{
  "action": "start"
}
```

To stop your control logic, use the following command input:

```json
{
  "action": "stop"
}
```
