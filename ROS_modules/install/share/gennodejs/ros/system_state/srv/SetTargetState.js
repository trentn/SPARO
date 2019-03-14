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

class SetTargetStateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.json_desiredstate = null;
    }
    else {
      if (initObj.hasOwnProperty('json_desiredstate')) {
        this.json_desiredstate = initObj.json_desiredstate
      }
      else {
        this.json_desiredstate = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetTargetStateRequest
    // Serialize message field [json_desiredstate]
    bufferOffset = _serializer.string(obj.json_desiredstate, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTargetStateRequest
    let len;
    let data = new SetTargetStateRequest(null);
    // Deserialize message field [json_desiredstate]
    data.json_desiredstate = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.json_desiredstate.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/SetTargetStateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ea98535ee80b092d18bf0793fe5f2f75';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string json_desiredstate
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetTargetStateRequest(null);
    if (msg.json_desiredstate !== undefined) {
      resolved.json_desiredstate = msg.json_desiredstate;
    }
    else {
      resolved.json_desiredstate = ''
    }

    return resolved;
    }
};

class SetTargetStateResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state_reached = null;
    }
    else {
      if (initObj.hasOwnProperty('state_reached')) {
        this.state_reached = initObj.state_reached
      }
      else {
        this.state_reached = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetTargetStateResponse
    // Serialize message field [state_reached]
    bufferOffset = _serializer.int8(obj.state_reached, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTargetStateResponse
    let len;
    let data = new SetTargetStateResponse(null);
    // Deserialize message field [state_reached]
    data.state_reached = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/SetTargetStateResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd14741f21a107d8dfdecf2120a39d20d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 state_reached
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetTargetStateResponse(null);
    if (msg.state_reached !== undefined) {
      resolved.state_reached = msg.state_reached;
    }
    else {
      resolved.state_reached = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: SetTargetStateRequest,
  Response: SetTargetStateResponse,
  md5sum() { return 'e48ef780cf73cc26b8047ad6ac36082b'; },
  datatype() { return 'system_state/SetTargetState'; }
};
