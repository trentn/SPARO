// Auto-generated. Do not edit!

// (in-package system_state.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class MoveRobotRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.X = null;
      this.Y = null;
    }
    else {
      if (initObj.hasOwnProperty('X')) {
        this.X = initObj.X
      }
      else {
        this.X = 0;
      }
      if (initObj.hasOwnProperty('Y')) {
        this.Y = initObj.Y
      }
      else {
        this.Y = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveRobotRequest
    // Serialize message field [X]
    bufferOffset = _serializer.int64(obj.X, buffer, bufferOffset);
    // Serialize message field [Y]
    bufferOffset = _serializer.int64(obj.Y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveRobotRequest
    let len;
    let data = new MoveRobotRequest(null);
    // Deserialize message field [X]
    data.X = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [Y]
    data.Y = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/MoveRobotRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6dab1705b6ff76dc460c7c88a89a4a61';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 X
    int64 Y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveRobotRequest(null);
    if (msg.X !== undefined) {
      resolved.X = msg.X;
    }
    else {
      resolved.X = 0
    }

    if (msg.Y !== undefined) {
      resolved.Y = msg.Y;
    }
    else {
      resolved.Y = 0
    }

    return resolved;
    }
};

class MoveRobotResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.reached_position = null;
    }
    else {
      if (initObj.hasOwnProperty('reached_position')) {
        this.reached_position = initObj.reached_position
      }
      else {
        this.reached_position = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveRobotResponse
    // Serialize message field [reached_position]
    bufferOffset = _serializer.bool(obj.reached_position, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveRobotResponse
    let len;
    let data = new MoveRobotResponse(null);
    // Deserialize message field [reached_position]
    data.reached_position = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/MoveRobotResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ad0686c29d6de7db1f1ccb258f723d7f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool reached_position
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveRobotResponse(null);
    if (msg.reached_position !== undefined) {
      resolved.reached_position = msg.reached_position;
    }
    else {
      resolved.reached_position = false
    }

    return resolved;
    }
};

module.exports = {
  Request: MoveRobotRequest,
  Response: MoveRobotResponse,
  md5sum() { return '5aa155b242bcdec0a89321f704bbe675'; },
  datatype() { return 'system_state/MoveRobot'; }
};
