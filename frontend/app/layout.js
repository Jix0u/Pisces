import { inter, roboto_condensed } from './fonts'
import './globals.css'

export const metadata = {
  title: 'Pisces',
  description: 'The All in One Marketing Solution',
}

export default function RootLayout({ children }) {
  return (
    <html lang='en'>
      <body className={inter.className}>{children}</body>
    </html>
  )
}
