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

class DetectTargetRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DetectTargetRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DetectTargetRequest
    let len;
    let data = new DetectTargetRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/DetectTargetRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DetectTargetRequest(null);
    return resolved;
    }
};

class DetectTargetResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.json_state = null;
      this.X = null;
      this.Y = null;
      this.Z = null;
    }
    else {
      if (initObj.hasOwnProperty('json_state')) {
        this.json_state = initObj.json_state
      }
      else {
        this.json_state = '';
      }
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
    // Serializes a message object of type DetectTargetResponse
    // Serialize message field [json_state]
    bufferOffset = _serializer.string(obj.json_state, buffer, bufferOffset);
    // Serialize message field [X]
    bufferOffset = _serializer.int64(obj.X, buffer, bufferOffset);
    // Serialize message field [Y]
    bufferOffset = _serializer.int64(obj.Y, buffer, bufferOffset);
    // Serialize message field [Z]
    bufferOffset = _serializer.int64(obj.Z, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DetectTargetResponse
    let len;
    let data = new DetectTargetResponse(null);
    // Deserialize message field [json_state]
    data.json_state = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [X]
    data.X = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [Y]
    data.Y = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [Z]
    data.Z = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.json_state.length;
    return length + 28;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/DetectTargetResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '771f4495ccebaf28e2e698ac883f1d20';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string json_state
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
    const resolved = new DetectTargetResponse(null);
    if (msg.json_state !== undefined) {
      resolved.json_state = msg.json_state;
    }
    else {
      resolved.json_state = ''
    }

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

module.exports = {
  Request: DetectTargetRequest,
  Response: DetectTargetResponse,
  md5sum() { return '771f4495ccebaf28e2e698ac883f1d20'; },
  datatype() { return 'system_state/DetectTarget'; }
};
