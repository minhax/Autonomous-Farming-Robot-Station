// Generated by gencpp from file custom_msgs/PlantBox.msg
// DO NOT EDIT!


#ifndef CUSTOM_MSGS_MESSAGE_PLANTBOX_H
#define CUSTOM_MSGS_MESSAGE_PLANTBOX_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace custom_msgs
{
template <class ContainerAllocator>
struct PlantBox_
{
  typedef PlantBox_<ContainerAllocator> Type;

  PlantBox_()
    : x(0)
    , y(0)
    , length(0)
    , width(0)  {
    }
  PlantBox_(const ContainerAllocator& _alloc)
    : x(0)
    , y(0)
    , length(0)
    , width(0)  {
  (void)_alloc;
    }



   typedef uint32_t _x_type;
  _x_type x;

   typedef uint32_t _y_type;
  _y_type y;

   typedef uint32_t _length_type;
  _length_type length;

   typedef uint32_t _width_type;
  _width_type width;





  typedef boost::shared_ptr< ::custom_msgs::PlantBox_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::custom_msgs::PlantBox_<ContainerAllocator> const> ConstPtr;

}; // struct PlantBox_

typedef ::custom_msgs::PlantBox_<std::allocator<void> > PlantBox;

typedef boost::shared_ptr< ::custom_msgs::PlantBox > PlantBoxPtr;
typedef boost::shared_ptr< ::custom_msgs::PlantBox const> PlantBoxConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::custom_msgs::PlantBox_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::custom_msgs::PlantBox_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace custom_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'custom_msgs': ['/home/pi/Documents/ros_ws/src/custom_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::custom_msgs::PlantBox_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::custom_msgs::PlantBox_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::custom_msgs::PlantBox_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::custom_msgs::PlantBox_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_msgs::PlantBox_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_msgs::PlantBox_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::custom_msgs::PlantBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2c2b959d705840bcab8520e8edc01dee";
  }

  static const char* value(const ::custom_msgs::PlantBox_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2c2b959d705840bcULL;
  static const uint64_t static_value2 = 0xab8520e8edc01deeULL;
};

template<class ContainerAllocator>
struct DataType< ::custom_msgs::PlantBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "custom_msgs/PlantBox";
  }

  static const char* value(const ::custom_msgs::PlantBox_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::custom_msgs::PlantBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32 x\n\
uint32 y\n\
uint32 length\n\
uint32 width\n\
";
  }

  static const char* value(const ::custom_msgs::PlantBox_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::custom_msgs::PlantBox_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.length);
      stream.next(m.width);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlantBox_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::custom_msgs::PlantBox_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::custom_msgs::PlantBox_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y);
    s << indent << "length: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.length);
    s << indent << "width: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.width);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CUSTOM_MSGS_MESSAGE_PLANTBOX_H
