# Cards Against Humanity
> Play CAH directly in your browser with the power of WebRTC

## Play in your browser
*Note: the site is hosted on [Glitch.com](glitch.com). It may take a few seconds to start up.*
1. Ask the host (black card reader) to visit [this link](http://cah7.glitch.me/host)
2. Ask the host to copy and send the link generated
3. The players should automatically connect to the game

Mobile devices recommended

## To do
- [x] Shuffle cards. Currently, all users will get the same hand of white cards. The order of black cards is also the same.
- [ ] Handle disconnected users better.
- [ ] Find a way to "shuffle the deck and distribute cards" throught the sockets. Even when the cards are shuffled, there's a probability that two players get the same white cards. This will be a lot more difficult to fix.

## Built with
- NodeJS + Express
- Socket.IO
- HTML/CSS/JS (no frameworks)
- [JSON Against Humanity](https://www.crhallberg.com/cah/) (Using the base set)
- PeerJS
- Python (to generate arrays for the white and black cards)

## Support development
Download the Brave Browser using [this link](https://brave.com/pjb276)! Download and use it for a month.

It's like Chrome, but faster with built-in ad-blocking.

## License
GNU AGPLv3