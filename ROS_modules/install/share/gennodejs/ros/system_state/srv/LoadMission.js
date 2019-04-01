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

class LoadMissionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LoadMissionRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LoadMissionRequest
    let len;
    let data = new LoadMissionRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/LoadMissionRequest';
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
    const resolved = new LoadMissionRequest(null);
    return resolved;
    }
};

class LoadMissionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.json_mission = null;
    }
    else {
      if (initObj.hasOwnProperty('json_mission')) {
        this.json_mission = initObj.json_mission
      }
      else {
        this.json_mission = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LoadMissionResponse
    // Serialize message field [json_mission]
    bufferOffset = _serializer.string(obj.json_mission, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LoadMissionResponse
    let len;
    let data = new LoadMissionResponse(null);
    // Deserialize message field [json_mission]
    data.json_mission = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.json_mission.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'system_state/LoadMissionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cf76547124a8eccb32585a0d744f179b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string json_mission
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LoadMissionResponse(null);
    if (msg.json_mission !== undefined) {
      resolved.json_mission = msg.json_mission;
    }
    else {
      resolved.json_mission = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: LoadMissionRequest,
  Response: LoadMissionResponse,
  md5sum() { return 'cf76547124a8eccb32585a0d744f179b'; },
  datatype() { return 'system_state/LoadMission'; }
};
