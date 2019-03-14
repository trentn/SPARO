;; Auto-generated. Do not edit!


(when (boundp 'system_state::MoveRobot)
  (if (not (find-package "SYSTEM_STATE"))
    (make-package "SYSTEM_STATE"))
  (shadow 'MoveRobot (find-package "SYSTEM_STATE")))
(unless (find-package "SYSTEM_STATE::MOVEROBOT")
  (make-package "SYSTEM_STATE::MOVEROBOT"))
(unless (find-package "SYSTEM_STATE::MOVEROBOTREQUEST")
  (make-package "SYSTEM_STATE::MOVEROBOTREQUEST"))
(unless (find-package "SYSTEM_STATE::MOVEROBOTRESPONSE")
  (make-package "SYSTEM_STATE::MOVEROBOTRESPONSE"))

(in-package "ROS")





(defclass system_state::MoveRobotRequest
  :super ros::object
  :slots (_X _Y ))

(defmethod system_state::MoveRobotRequest
  (:init
   (&key
    ((:X __X) 0)
    ((:Y __Y) 0)
    )
   (send-super :init)
   (setq _X (round __X))
   (setq _Y (round __Y))
   self)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:serialization-length
   ()
   (+
    ;; int64 _X
    8
    ;; int64 _Y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _X
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _X (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _X) (= (length (_X . bv)) 2)) ;; bignum
              (write-long (ash (elt (_X . bv) 0) 0) s)
              (write-long (ash (elt (_X . bv) 1) -1) s))
             ((and (class _X) (= (length (_X . bv)) 1)) ;; big1
              (write-long (elt (_X . bv) 0) s)
              (write-long (if (>= _X 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _X s)(write-long (if (>= _X 0) 0 #xffffffff) s)))
     ;; int64 _Y
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _Y (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _Y) (= (length (_Y . bv)) 2)) ;; bignum
              (write-long (ash (elt (_Y . bv) 0) 0) s)
              (write-long (ash (elt (_Y . bv) 1) -1) s))
             ((and (class _Y) (= (length (_Y . bv)) 1)) ;; big1
              (write-long (elt (_Y . bv) 0) s)
              (write-long (if (>= _Y 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _Y s)(write-long (if (>= _Y 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _X
#+(or :alpha :irix6 :x86_64)
      (setf _X (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _X (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _Y
#+(or :alpha :irix6 :x86_64)
      (setf _Y (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _Y (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass system_state::MoveRobotResponse
  :super ros::object
  :slots (_reached_position ))

(defmethod system_state::MoveRobotResponse
  (:init
   (&key
    ((:reached_position __reached_position) nil)
    )
   (send-super :init)
   (setq _reached_position __reached_position)
   self)
  (:reached_position
   (&optional __reached_position)
   (if __reached_position (setq _reached_position __reached_position)) _reached_position)
  (:serialization-length
   ()
   (+
    ;; bool _reached_position
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _reached_position
       (if _reached_position (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _reached_position
     (setq _reached_position (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass system_state::MoveRobot
  :super ros::object
  :slots ())

(setf (get system_state::MoveRobot :md5sum-) "5aa155b242bcdec0a89321f704bbe675")
(setf (get system_state::MoveRobot :datatype-) "system_state/MoveRobot")
(setf (get system_state::MoveRobot :request) system_state::MoveRobotRequest)
(setf (get system_state::MoveRobot :response) system_state::MoveRobotResponse)

(defmethod system_state::MoveRobotRequest
  (:response () (instance system_state::MoveRobotResponse :init)))

(setf (get system_state::MoveRobotRequest :md5sum-) "5aa155b242bcdec0a89321f704bbe675")
(setf (get system_state::MoveRobotRequest :datatype-) "system_state/MoveRobotRequest")
(setf (get system_state::MoveRobotRequest :definition-)
      "int64 X
int64 Y
---
bool reached_position
")

(setf (get system_state::MoveRobotResponse :md5sum-) "5aa155b242bcdec0a89321f704bbe675")
(setf (get system_state::MoveRobotResponse :datatype-) "system_state/MoveRobotResponse")
(setf (get system_state::MoveRobotResponse :definition-)
      "int64 X
int64 Y
---
bool reached_position
")



(provide :system_state/MoveRobot "5aa155b242bcdec0a89321f704bbe675")


