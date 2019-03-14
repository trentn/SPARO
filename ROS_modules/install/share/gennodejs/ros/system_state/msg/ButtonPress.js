// Auto-generated. Do not edit!

// (in-package system_state.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ButtonPress {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.button_pressed = null;
    }
    else {
      if (initObj.hasOwnProperty('button_pressed')) {
        this.button_pressed = initObj.button_pressed
      }
      else {
        this.button_pressed = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ButtonPress
    // Serialize message field [button_pressed]
    bufferOffset = _serializer.string(obj.button_pressed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ButtonPress
    let len;
    let data = new ButtonPress(null);
    // Deserialize message field [button_pressed]
    data.button_pressed = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.button_pressed.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'system_state/ButtonPress';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '15623fe39de8b6cd03b18644d7b7c594';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string button_pressed
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ButtonPress(null);
    if (msg.button_pressed !== undefined) {
      resolved.button_pressed = msg.button_pressed;
    }
    else {
      resolved.button_pressed = ''
    }

    return resolved;
    }
};

module.exports = ButtonPress;
