; Auto-generated. Do not edit!


(cl:in-package system_state-srv)


;//! \htmlinclude SetTargetState-request.msg.html

(cl:defclass <SetTargetState-request> (roslisp-msg-protocol:ros-message)
  ((json_desiredstate
    :reader json_desiredstate
    :initarg :json_desiredstate
    :type cl:string
    :initform ""))
)

(cl:defclass SetTargetState-request (<SetTargetState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTargetState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTargetState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<SetTargetState-request> is deprecated: use system_state-srv:SetTargetState-request instead.")))

(cl:ensure-generic-function 'json_desiredstate-val :lambda-list '(m))
(cl:defmethod json_desiredstate-val ((m <SetTargetState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:json_desiredstate-val is deprecated.  Use system_state-srv:json_desiredstate instead.")
  (json_desiredstate m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTargetState-request>) ostream)
  "Serializes a message object of type '<SetTargetState-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_desiredstate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_desiredstate))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTargetState-request>) istream)
  "Deserializes a message object of type '<SetTargetState-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_desiredstate) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_desiredstate) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTargetState-request>)))
  "Returns string type for a service object of type '<SetTargetState-request>"
  "system_state/SetTargetStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTargetState-request)))
  "Returns string type for a service object of type 'SetTargetState-request"
  "system_state/SetTargetStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTargetState-request>)))
  "Returns md5sum for a message object of type '<SetTargetState-request>"
  "e48ef780cf73cc26b8047ad6ac36082b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTargetState-request)))
  "Returns md5sum for a message object of type 'SetTargetState-request"
  "e48ef780cf73cc26b8047ad6ac36082b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTargetState-request>)))
  "Returns full string definition for message of type '<SetTargetState-request>"
  (cl:format cl:nil "string json_desiredstate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTargetState-request)))
  "Returns full string definition for message of type 'SetTargetState-request"
  (cl:format cl:nil "string json_desiredstate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTargetState-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'json_desiredstate))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTargetState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTargetState-request
    (cl:cons ':json_desiredstate (json_desiredstate msg))
))
;//! \htmlinclude SetTargetState-response.msg.html

(cl:defclass <SetTargetState-response> (roslisp-msg-protocol:ros-message)
  ((state_reached
    :reader state_reached
    :initarg :state_reached
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SetTargetState-response (<SetTargetState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTargetState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTargetState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<SetTargetState-response> is deprecated: use system_state-srv:SetTargetState-response instead.")))

(cl:ensure-generic-function 'state_reached-val :lambda-list '(m))
(cl:defmethod state_reached-val ((m <SetTargetState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:state_reached-val is deprecated.  Use system_state-srv:state_reached instead.")
  (state_reached m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTargetState-response>) ostream)
  "Serializes a message object of type '<SetTargetState-response>"
  (cl:let* ((signed (cl:slot-value msg 'state_reached)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTargetState-response>) istream)
  "Deserializes a message object of type '<SetTargetState-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_reached) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTargetState-response>)))
  "Returns string type for a service object of type '<SetTargetState-response>"
  "system_state/SetTargetStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTargetState-response)))
  "Returns string type for a service object of type 'SetTargetState-response"
  "system_state/SetTargetStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTargetState-response>)))
  "Returns md5sum for a message object of type '<SetTargetState-response>"
  "e48ef780cf73cc26b8047ad6ac36082b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTargetState-response)))
  "Returns md5sum for a message object of type 'SetTargetState-response"
  "e48ef780cf73cc26b8047ad6ac36082b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTargetState-response>)))
  "Returns full string definition for message of type '<SetTargetState-response>"
  (cl:format cl:nil "int8 state_reached~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTargetState-response)))
  "Returns full string definition for message of type 'SetTargetState-response"
  (cl:format cl:nil "int8 state_reached~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTargetState-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTargetState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTargetState-response
    (cl:cons ':state_reached (state_reached msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetTargetState)))
  'SetTargetState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetTargetState)))
  'SetTargetState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTargetState)))
  "Returns string type for a service object of type '<SetTargetState>"
  "system_state/SetTargetState")