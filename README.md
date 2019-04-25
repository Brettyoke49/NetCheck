# NetCheck
Network information monitoring tool

To check usage of either program (client or server) use the -h flag.

Set up two linux computers over a network. Have one start up the server with the desired IP and port.
Have the other start up the client, providing normal duration(in seconds), DoS duration (in seconds), and then the desired IP and port.

Default IP and port are localhost and 9099.
Durations are 60 seconds by default.

Do not stop either the client or server early or you will not get accurate results.
After the client finishes running the server will present the user with summary statistics on how the client and server performed over the network.
