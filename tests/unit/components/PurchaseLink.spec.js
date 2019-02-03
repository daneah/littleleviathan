import { shallowMount } from '@vue/test-utils'

import PurchaseLink from '@/components/PurchaseLink'


describe('PurchaseLink', () => {
  let wrapper

  beforeEach(() => {
    wrapper = shallowMount(PurchaseLink, {
      propsData: {
        href: 'https://link.biz',
        service: 'Musix',
        icon: 'the-icon',
      },
      stubs: {
        FontAwesome: '<div class="fa-stub"></div>',
      },
    })
  })

  it('Renders a link', () => {
    expect(wrapper.isVueInstance()).toBe(true)
    expect(wrapper.is('a')).toBe(true)
  })

  it('Uses the passed in props', () => {
    expect(wrapper.find('a').attributes('href')).toBe('https://link.biz')
    expect(wrapper.find('a').attributes('title')).toBe('Listen on Musix')
    expect(wrapper.find('.fa-stub').attributes('icon')).toBe('the-icon')
  })
})
