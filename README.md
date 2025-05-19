# VCL Tournament Overlay - Lazer edition by [FukutoTojido](https://github.com/FukutoTojido)
___
## [**Overlay preview**](https://www.twitch.tv/videos/1445278730?collection=vyL2iPlp4xYysw&t=00h11m56s)

## Why this thing exists?
- You hate configuring Lazer
- You want the same look that Lazer provides but want to spend less time setting things up
- You prefer the ease of customizing an open-source overlay

## Setup guide:
- Install [**Tosu**](https://github.com/KotRikD/tosu/releases/latest)
- Download this repo as .zip and extract to `static` folder of Tosu
- Rename either `index_acc.js` or `index_score.js` to `index.js`, depends on which win condition you are using
- Update `\mappool\beatmaps.json` to match your mappool
- Update `\mappool\beatmap_data.json` using the script in `beatmap_data generator` folder

## Styling
- Change mod icons in `\mappool\static` folder
- Change background in `\static` folder (`mp-bg` for Gameplay, `mp-bg2` for Mappool)
- There are 2 CSS files to choose whether you want team image / profile picture to show or not. See `css` folder and remove/rename `topBar.css` accordingly.
	- The default `topBar.css` enables showing images, while the other one doesn't.
- Most colors can be found in `\css\style.css`
- For P1/P2 score, change hex code in `index.js` (Line `253` for P1 and line `266` for P2)

## Overlay interaction (in OBS)
- Add a browser source in OBS:
  - URL: `127.0.0.1:24050/vcl-tournament-overlay`
  - Width: `2420`
  - Height: `1080`

- Click on `Interact` button below the preview to interact with the overlay
- Picks: Left click for P1, right click for P2
- Bans: Shift + Left click for P1, Shift + Right click for P2
- Reset map status: Ctrl + Click
> Note that bans are manual. Once done, you can set First Pick team in the Interact window to start the auto-pick process.

## Notes
- To trigger the auto-switching between gameplay and mappool, **score announce message must contain `Next Pick: ...` phrase (case sensitive).** Of course with some code digging you can find where to change this.
- If the players' avatars are not visible, spam Refresh in OBS.
___
- For additional support, DM `hoaq#6054` on Discord (or ping in osu! Tournament Hub) - note that any requests regarding modifying overlay design will be ignored.
- If you are modifying this overlay, **please make a fork** so we know which tournament this is being used for :D
