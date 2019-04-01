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

class MoveEndEffectorRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.X = null;
      this.Y = null;
      this.Z = null;
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
      if (initObj.hasOwnProperty('Z')) {
        this.Z = initObj.Z
      }
      else {
        this.Z = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveEndEffectorRequest
    // Serialize message field [X]
    bufferOffset = _serializer.int64(obj.X, buffer, bufferOffset);
    // Serialize message field [Y]
    bufferOffset = _serializer.int64(obj.Y, buffer, bufferOffset);
    // Serialize message field [Z]
    bufferOffset = _serializer.int64(obj.Z, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveEndEffectorRequest
    let len;
    let data = new MoveEndEffectorRequest(null);
    // Deserialize message field [X]
    data.X = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [Y]
    data.Y = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [Z]
    data.Z = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/MoveEndEffectorRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ddce4ba898b1cdeed19df4a3f2519794';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 X
    int64 Y
    int64 Z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveEndEffectorRequest(null);
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

    if (msg.Z !== undefined) {
      resolved.Z = msg.Z;
    }
    else {
      resolved.Z = 0
    }

    return resolved;
    }
};

class MoveEndEffectorResponse {
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
    // Serializes a message object of type MoveEndEffectorResponse
    // Serialize message field [reached_position]
    bufferOffset = _serializer.bool(obj.reached_position, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveEndEffectorResponse
    let len;
    let data = new MoveEndEffectorResponse(null);
    // Deserialize message field [reached_position]
    data.reached_position = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/MoveEndEffectorResponse';
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
    const resolved = new MoveEndEffectorResponse(null);
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
  Request: MoveEndEffectorRequest,
  Response: MoveEndEffectorResponse,
  md5sum() { return '515108492c7d4ad3a4f126e6820b3140'; },
  datatype() { return 'system_state/MoveEndEffector'; }
};
