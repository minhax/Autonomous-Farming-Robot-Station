// Auto-generated. Do not edit!

// (in-package custom_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class SerialPacket {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Code = null;
      this.Length = null;
      this.Buffer = null;
    }
    else {
      if (initObj.hasOwnProperty('Code')) {
        this.Code = initObj.Code
      }
      else {
        this.Code = 0;
      }
      if (initObj.hasOwnProperty('Length')) {
        this.Length = initObj.Length
      }
      else {
        this.Length = 0;
      }
      if (initObj.hasOwnProperty('Buffer')) {
        this.Buffer = initObj.Buffer
      }
      else {
        this.Buffer = new Array(64).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SerialPacket
    // Serialize message field [Code]
    bufferOffset = _serializer.uint16(obj.Code, buffer, bufferOffset);
    // Serialize message field [Length]
    bufferOffset = _serializer.uint16(obj.Length, buffer, bufferOffset);
    // Check that the constant length array field [Buffer] has the right length
    if (obj.Buffer.length !== 64) {
      throw new Error('Unable to serialize array field Buffer - length must be 64')
    }
    // Serialize message field [Buffer]
    bufferOffset = _arraySerializer.uint8(obj.Buffer, buffer, bufferOffset, 64);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SerialPacket
    let len;
    let data = new SerialPacket(null);
    // Deserialize message field [Code]
    data.Code = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [Length]
    data.Length = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [Buffer]
    data.Buffer = _arrayDeserializer.uint8(buffer, bufferOffset, 64)
    return data;
  }

  static getMessageSize(object) {
    return 68;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msgs/SerialPacket';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c3caf2e11f9a4e075e8eb559468402d7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 Code
    uint16 Length
    uint8[64] Buffer
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SerialPacket(null);
    if (msg.Code !== undefined) {
      resolved.Code = msg.Code;
    }
    else {
      resolved.Code = 0
    }

    if (msg.Length !== undefined) {
      resolved.Length = msg.Length;
    }
    else {
      resolved.Length = 0
    }

    if (msg.Buffer !== undefined) {
      resolved.Buffer = msg.Buffer;
    }
    else {
      resolved.Buffer = new Array(64).fill(0)
    }

    return resolved;
    }
};

module.exports = SerialPacket;
