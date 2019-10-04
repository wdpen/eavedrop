import random, getpass, sys, asyncio, os
import playground
from playground.network.packet.fieldtypes import STRING, BUFFER, UINT8, UINT16, BOOL
from playground.network.common import PlaygroundAddress
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes.attributes import Optional
from playground.common.logging import EnablePresetLogging, PRESET_DEBUG, PRESET_VERBOSE
#from prfc_packet import *
#from escape_room_006 import *

EnablePresetLogging(PRESET_DEBUG)


from playground.network.protocols.vsockets import VNICDumpProtocol
from playground.network.protocols.packets.switching_packets import WirePacket

class eavesdrop(VNICDumpProtocol):
	def data_received(self,data):
		dd=WirePacket.Deserializer()
		dd.update(data)
		for recvpack in dd.nextPackets():
			print(recvpack.source, recvpack.sourcePort, recvpack.destination, recvpack.destinationPort)
			dd2=PacketType.Deserializer()
			dd2.update(recvpack.data)
			for pac in dd2.nextPackets():
				print(pac)


if __name__=='__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(playground.connect.raw_vnic_connection(eavesdrop()))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		loop.stop()
		loop.close()