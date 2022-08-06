# Totally-Ordered-Multicast

The totally ordered multicast protocol based on Lamport's logical clocks.

The simulated process will first initialize its local clock as 0 and then start waiting for event entries by
the end-user.

There will be 3 options:
 Send new message m: ask for the message text, generate and display the globally unique message ID and message timestamp.

 Receive message m from process i: ask for the message text, the globally unique message ID, message timestamp, and sender's process identifier.

 Receive acknowledgement on message m: list the received messages and ask the user to pick the message to be acknowledged.
