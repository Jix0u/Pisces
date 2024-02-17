import { inter, roboto_condensed } from './fonts'
import Image from 'next/image'
import './index.css'

export default function Home() {
  return (
    <main>
      <nav>
        <div className='navLogo'>
          <a href=''>Pisces</a>
        </div>
        <div className='menu'>
          <p>Menu</p>
        </div>
        <div className='shop'>
          <a href=''>Shop</a>
          <a href=''>Cart</a>
        </div>
      </nav>

      <div className='hero'>
        <Image src={'/images/hero.jpg'} width={6000} height={4000} />
      </div>

      <div className='heroCopy'>
        <h1>Pisces</h1>
      </div>

      <div className='overlay'>
        <div className='overlayContent'>
          <div className='images'>
            <div className='imgHolder'>
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
              <Image
                src={'/images/loader.jpg'}
                width={550}
                height={550}
                className='loadImg'
              />
            </div>
          </div>

          <div className='text'>
            <div className='counter'>
              <p>100%</p>
            </div>
            <div className='logo'>
              <p>Kudos</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
