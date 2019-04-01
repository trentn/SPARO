;; Auto-generated. Do not edit!


(when (boundp 'system_state::ButtonPress)
  (if (not (find-package "SYSTEM_STATE"))
    (make-package "SYSTEM_STATE"))
  (shadow 'ButtonPress (find-package "SYSTEM_STATE")))
(unless (find-package "SYSTEM_STATE::BUTTONPRESS")
  (make-package "SYSTEM_STATE::BUTTONPRESS"))

(in-package "ROS")
;;//! \htmlinclude ButtonPress.msg.html


(defclass system_state::ButtonPress
  :super ros::object
  :slots (_button_pressed ))

(defmethod system_state::ButtonPress
  (:init
   (&key
    ((:button_pressed __button_pressed) "")
    )
   (send-super :init)
   (setq _button_pressed (string __button_pressed))
   self)
  (:button_pressed
   (&optional __button_pressed)
   (if __button_pressed (setq _button_pressed __button_pressed)) _button_pressed)
  (:serialization-length
   ()
   (+
    ;; string _button_pressed
    4 (length _button_pressed)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _button_pressed
       (write-long (length _button_pressed) s) (princ _button_pressed s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _button_pressed
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _button_pressed (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get system_state::ButtonPress :md5sum-) "15623fe39de8b6cd03b18644d7b7c594")
(setf (get system_state::ButtonPress :datatype-) "system_state/ButtonPress")
(setf (get system_state::ButtonPress :definition-)
      "string button_pressed
")



(provide :system_state/ButtonPress "15623fe39de8b6cd03b18644d7b7c594")


