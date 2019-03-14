// Generated by gencpp from file system_state/ButtonPress.msg
// DO NOT EDIT!


#ifndef SYSTEM_STATE_MESSAGE_BUTTONPRESS_H
#define SYSTEM_STATE_MESSAGE_BUTTONPRESS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace system_state
{
template <class ContainerAllocator>
struct ButtonPress_
{
  typedef ButtonPress_<ContainerAllocator> Type;

  ButtonPress_()
    : button_pressed()  {
    }
  ButtonPress_(const ContainerAllocator& _alloc)
    : button_pressed(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _button_pressed_type;
  _button_pressed_type button_pressed;





  typedef boost::shared_ptr< ::system_state::ButtonPress_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::system_state::ButtonPress_<ContainerAllocator> const> ConstPtr;

}; // struct ButtonPress_

typedef ::system_state::ButtonPress_<std::allocator<void> > ButtonPress;

typedef boost::shared_ptr< ::system_state::ButtonPress > ButtonPressPtr;
typedef boost::shared_ptr< ::system_state::ButtonPress const> ButtonPressConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::system_state::ButtonPress_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::system_state::ButtonPress_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace system_state

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'system_state': ['/home/ubuntu/SPARO/ROS_modules/src/system_state/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::system_state::ButtonPress_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::system_state::ButtonPress_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::system_state::ButtonPress_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::system_state::ButtonPress_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::system_state::ButtonPress_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::system_state::ButtonPress_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::system_state::ButtonPress_<ContainerAllocator> >
{
  static const char* value()
  {
    return "15623fe39de8b6cd03b18644d7b7c594";
  }

  static const char* value(const ::system_state::ButtonPress_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x15623fe39de8b6cdULL;
  static const uint64_t static_value2 = 0x03b18644d7b7c594ULL;
};

template<class ContainerAllocator>
struct DataType< ::system_state::ButtonPress_<ContainerAllocator> >
{
  static const char* value()
  {
    return "system_state/ButtonPress";
  }

  static const char* value(const ::system_state::ButtonPress_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::system_state::ButtonPress_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string button_pressed\n\
";
  }

  static const char* value(const ::system_state::ButtonPress_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::system_state::ButtonPress_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.button_pressed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ButtonPress_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::system_state::ButtonPress_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::system_state::ButtonPress_<ContainerAllocator>& v)
  {
    s << indent << "button_pressed: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.button_pressed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SYSTEM_STATE_MESSAGE_BUTTONPRESS_H
