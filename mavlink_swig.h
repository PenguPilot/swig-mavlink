
#ifndef __MAVLINK_SWIG_H__
#define __MAVLINK_SWIG_H__


inline PyObject *mavlink_dumps(const mavlink_message_t *msg)
{
   char buffer[1024];
   memcpy(buffer, (const uint8_t *)&msg->magic, MAVLINK_NUM_HEADER_BYTES + (uint16_t)msg->len);
   uint8_t *ck = buffer + (MAVLINK_NUM_HEADER_BYTES + (uint16_t)msg->len);
   ck[0] = (uint8_t)(msg->checksum & 0xFF);
   ck[1] = (uint8_t)(msg->checksum >> 8);
   return PyString_FromStringAndSize(buffer, MAVLINK_NUM_NON_PAYLOAD_BYTES + (uint16_t)msg->len);
}



#endif /* __MAVLINK_SWIG_H__ */

