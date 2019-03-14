// Generated by gencpp from file system_state/SetTargetState.msg
// DO NOT EDIT!


#ifndef SYSTEM_STATE_MESSAGE_SETTARGETSTATE_H
#define SYSTEM_STATE_MESSAGE_SETTARGETSTATE_H

#include <ros/service_traits.h>


#include <system_state/SetTargetStateRequest.h>
#include <system_state/SetTargetStateResponse.h>


namespace system_state
{

struct SetTargetState
{

typedef SetTargetStateRequest Request;
typedef SetTargetStateResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetTargetState
} // namespace system_state


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::system_state::SetTargetState > {
  static const char* value()
  {
    return "e48ef780cf73cc26b8047ad6ac36082b";
  }

  static const char* value(const ::system_state::SetTargetState&) { return value(); }
};

template<>
struct DataType< ::system_state::SetTargetState > {
  static const char* value()
  {
    return "system_state/SetTargetState";
  }

  static const char* value(const ::system_state::SetTargetState&) { return value(); }
};


// service_traits::MD5Sum< ::system_state::SetTargetStateRequest> should match 
// service_traits::MD5Sum< ::system_state::SetTargetState > 
template<>
struct MD5Sum< ::system_state::SetTargetStateRequest>
{
  static const char* value()
  {
    return MD5Sum< ::system_state::SetTargetState >::value();
  }
  static const char* value(const ::system_state::SetTargetStateRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::system_state::SetTargetStateRequest> should match 
// service_traits::DataType< ::system_state::SetTargetState > 
template<>
struct DataType< ::system_state::SetTargetStateRequest>
{
  static const char* value()
  {
    return DataType< ::system_state::SetTargetState >::value();
  }
  static const char* value(const ::system_state::SetTargetStateRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::system_state::SetTargetStateResponse> should match 
// service_traits::MD5Sum< ::system_state::SetTargetState > 
template<>
struct MD5Sum< ::system_state::SetTargetStateResponse>
{
  static const char* value()
  {
    return MD5Sum< ::system_state::SetTargetState >::value();
  }
  static const char* value(const ::system_state::SetTargetStateResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::system_state::SetTargetStateResponse> should match 
// service_traits::DataType< ::system_state::SetTargetState > 
template<>
struct DataType< ::system_state::SetTargetStateResponse>
{
  static const char* value()
  {
    return DataType< ::system_state::SetTargetState >::value();
  }
  static const char* value(const ::system_state::SetTargetStateResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SYSTEM_STATE_MESSAGE_SETTARGETSTATE_H
