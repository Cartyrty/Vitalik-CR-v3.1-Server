from Packets.Messages.Client.LoginMessage import Login
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage

packets = {
    10101: Login,
    10108: KeepAliveMessage
}
