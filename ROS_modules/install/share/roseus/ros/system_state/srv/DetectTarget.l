;; Auto-generated. Do not edit!


(when (boundp 'system_state::DetectTarget)
  (if (not (find-package "SYSTEM_STATE"))
    (make-package "SYSTEM_STATE"))
  (shadow 'DetectTarget (find-package "SYSTEM_STATE")))
(unless (find-package "SYSTEM_STATE::DETECTTARGET")
  (make-package "SYSTEM_STATE::DETECTTARGET"))
(unless (find-package "SYSTEM_STATE::DETECTTARGETREQUEST")
  (make-package "SYSTEM_STATE::DETECTTARGETREQUEST"))
(unless (find-package "SYSTEM_STATE::DETECTTARGETRESPONSE")
  (make-package "SYSTEM_STATE::DETECTTARGETRESPONSE"))

(in-package "ROS")





(defclass system_state::DetectTargetRequest
  :super ros::object
  :slots ())

(defmethod system_state::DetectTargetRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass system_state::DetectTargetResponse
  :super ros::object
  :slots (_json_state _X _Y _Z ))

(defmethod system_state::DetectTargetResponse
  (:init
   (&key
    ((:json_state __json_state) "")
    ((:X __X) 0)
    ((:Y __Y) 0)
    ((:Z __Z) 0)
    )
   (send-super :init)
   (setq _json_state (string __json_state))
   (setq _X (round __X))
   (setq _Y (round __Y))
   (setq _Z (round __Z))
   self)
  (:json_state
   (&optional __json_state)
   (if __json_state (setq _json_state __json_state)) _json_state)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:Z
   (&optional __Z)
   (if __Z (setq _Z __Z)) _Z)
  (:serialization-length
   ()
   (+
    ;; string _json_state
    4 (length _json_state)
    ;; int64 _X
    8
    ;; int64 _Y
    8
    ;; int64 _Z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _json_state
       (write-long (length _json_state) s) (princ _json_state s)
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
     ;; int64 _Z
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _Z (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _Z) (= (length (_Z . bv)) 2)) ;; bignum
              (write-long (ash (elt (_Z . bv) 0) 0) s)
              (write-long (ash (elt (_Z . bv) 1) -1) s))
             ((and (class _Z) (= (length (_Z . bv)) 1)) ;; big1
              (write-long (elt (_Z . bv) 0) s)
              (write-long (if (>= _Z 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _Z s)(write-long (if (>= _Z 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _json_state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
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
   ;; int64 _Z
#+(or :alpha :irix6 :x86_64)
      (setf _Z (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _Z (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
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

(defclass system_state::DetectTarget
  :super ros::object
  :slots ())

(setf (get system_state::DetectTarget :md5sum-) "771f4495ccebaf28e2e698ac883f1d20")
(setf (get system_state::DetectTarget :datatype-) "system_state/DetectTarget")
(setf (get system_state::DetectTarget :request) system_state::DetectTargetRequest)
(setf (get system_state::DetectTarget :response) system_state::DetectTargetResponse)

(defmethod system_state::DetectTargetRequest
  (:response () (instance system_state::DetectTargetResponse :init)))

(setf (get system_state::DetectTargetRequest :md5sum-) "771f4495ccebaf28e2e698ac883f1d20")
(setf (get system_state::DetectTargetRequest :datatype-) "system_state/DetectTargetRequest")
(setf (get system_state::DetectTargetRequest :definition-)
      "---
string json_state
int64 X
int64 Y
int64 Z
")

(setf (get system_state::DetectTargetResponse :md5sum-) "771f4495ccebaf28e2e698ac883f1d20")
(setf (get system_state::DetectTargetResponse :datatype-) "system_state/DetectTargetResponse")
(setf (get system_state::DetectTargetResponse :definition-)
      "---
string json_state
int64 X
int64 Y
int64 Z
")



(provide :system_state/DetectTarget "771f4495ccebaf28e2e698ac883f1d20")


