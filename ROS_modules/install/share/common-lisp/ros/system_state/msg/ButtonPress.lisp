; Auto-generated. Do not edit!


(cl:in-package system_state-msg)


;//! \htmlinclude ButtonPress.msg.html

(cl:defclass <ButtonPress> (roslisp-msg-protocol:ros-message)
  ((button_pressed
    :reader button_pressed
    :initarg :button_pressed
    :type cl:string
    :initform ""))
)

(cl:defclass ButtonPress (<ButtonPress>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ButtonPress>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ButtonPress)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-msg:<ButtonPress> is deprecated: use system_state-msg:ButtonPress instead.")))

(cl:ensure-generic-function 'button_pressed-val :lambda-list '(m))
(cl:defmethod button_pressed-val ((m <ButtonPress>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-msg:button_pressed-val is deprecated.  Use system_state-msg:button_pressed instead.")
  (button_pressed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ButtonPress>) ostream)
  "Serializes a message object of type '<ButtonPress>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'button_pressed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'button_pressed))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ButtonPress>) istream)
  "Deserializes a message object of type '<ButtonPress>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'button_pressed) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'button_pressed) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ButtonPress>)))
  "Returns string type for a message object of type '<ButtonPress>"
  "system_state/ButtonPress")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ButtonPress)))
  "Returns string type for a message object of type 'ButtonPress"
  "system_state/ButtonPress")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ButtonPress>)))
  "Returns md5sum for a message object of type '<ButtonPress>"
  "15623fe39de8b6cd03b18644d7b7c594")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ButtonPress)))
  "Returns md5sum for a message object of type 'ButtonPress"
  "15623fe39de8b6cd03b18644d7b7c594")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ButtonPress>)))
  "Returns full string definition for message of type '<ButtonPress>"
  (cl:format cl:nil "string button_pressed~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ButtonPress)))
  "Returns full string definition for message of type 'ButtonPress"
  (cl:format cl:nil "string button_pressed~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ButtonPress>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'button_pressed))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ButtonPress>))
  "Converts a ROS message object to a list"
  (cl:list 'ButtonPress
    (cl:cons ':button_pressed (button_pressed msg))
))
