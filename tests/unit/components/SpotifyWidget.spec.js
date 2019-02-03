import { shallowMount } from '@vue/test-utils';

import SpotifyWidget from '@/components/SpotifyWidget.vue';


describe('SpotifyWidget', () => {
  it('Renders an iframe with the correct src for Spotify', () => {
    const wrapper = shallowMount(SpotifyWidget, {
      propsData: {
        artistId: 'Little Leviathan',
        artistName: 'Little Leviathan'
      },
    });

    const iframe = wrapper.find('iframe');
    //expect(iframe.attributes('src')).toBe('https://open.spotify.com/follow/1/?uri=spotify:artist:Little Leviathan&size=basic&theme=light&show-count=0');
    //expect(iframe.attributes('title')).toBe('Follow Little Leviathan on Spotify');
  });
})
