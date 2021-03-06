// Generated by gencpp from file system_state/MoveEndEffectorRequest.msg
// DO NOT EDIT!


#ifndef SYSTEM_STATE_MESSAGE_MOVEENDEFFECTORREQUEST_H
#define SYSTEM_STATE_MESSAGE_MOVEENDEFFECTORREQUEST_H


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
struct MoveEndEffectorRequest_
{
  typedef MoveEndEffectorRequest_<ContainerAllocator> Type;

  MoveEndEffectorRequest_()
    : X(0)
    , Y(0)
    , Z(0)  {
    }
  MoveEndEffectorRequest_(const ContainerAllocator& _alloc)
    : X(0)
    , Y(0)
    , Z(0)  {
  (void)_alloc;
    }



   typedef int64_t _X_type;
  _X_type X;

   typedef int64_t _Y_type;
  _Y_type Y;

   typedef int64_t _Z_type;
  _Z_type Z;





  typedef boost::shared_ptr< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MoveEndEffectorRequest_

typedef ::system_state::MoveEndEffectorRequest_<std::allocator<void> > MoveEndEffectorRequest;

typedef boost::shared_ptr< ::system_state::MoveEndEffectorRequest > MoveEndEffectorRequestPtr;
typedef boost::shared_ptr< ::system_state::MoveEndEffectorRequest const> MoveEndEffectorRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::system_state::MoveEndEffectorRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace system_state

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'system_state': ['/home/ubuntu/SPARO/ROS_modules/src/system_state/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ddce4ba898b1cdeed19df4a3f2519794";
  }

  static const char* value(const ::system_state::MoveEndEffectorRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xddce4ba898b1cdeeULL;
  static const uint64_t static_value2 = 0xd19df4a3f2519794ULL;
};

template<class ContainerAllocator>
struct DataType< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "system_state/MoveEndEffectorRequest";
  }

  static const char* value(const ::system_state::MoveEndEffectorRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 X\n\
int64 Y\n\
int64 Z\n\
";
  }

  static const char* value(const ::system_state::MoveEndEffectorRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.X);
      stream.next(m.Y);
      stream.next(m.Z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveEndEffectorRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::system_state::MoveEndEffectorRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::system_state::MoveEndEffectorRequest_<ContainerAllocator>& v)
  {
    s << indent << "X: ";
    Printer<int64_t>::stream(s, indent + "  ", v.X);
    s << indent << "Y: ";
    Printer<int64_t>::stream(s, indent + "  ", v.Y);
    s << indent << "Z: ";
    Printer<int64_t>::stream(s, indent + "  ", v.Z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SYSTEM_STATE_MESSAGE_MOVEENDEFFECTORREQUEST_H
