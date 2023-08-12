import { defineStore } from 'pinia'

export const useAlbumStore = defineStore('albums', {
  state: () => ({
    albums: [
      {
        title: 'Little Leviathan',
        releaseYear: 2018,
        description: `Little Leviathan is the stage name and debut album title for singer/songwriter
        Dane Hillard. Dane grew up in northern Michigan and is inspired in part by the beautiful
        nature of those surroundings. The work in Little Leviathan is comprised of material written
        over the last seven years, and as a result of organic inspiration each song is true and
        untouched by the stresses of imminent release. The text explores ideas along the spectrum of
        love and loss, drawing from personal experience and observation.`,
        coverImage: 'little-leviathan-album-cover.jpg',
        spotifyId: '1YIFk8dmiw2W1JHOSRptcS',
        bandcampId: 'little-leviathan-2',
        soundcloudSet: 'little-leviathan',
        appleMusicLink: 'little-leviathan/id978903092'
      }
    ]
  })
})
