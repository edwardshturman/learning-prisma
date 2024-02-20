import { Hono } from 'hono'

const app = new Hono()

app.get('/', (c) => {
  if (c.req.query('amogus'))
    return c.text('sus')
  return c.text('not sus')
})

app.get('/jsx', (c) => {
  return c.html(
    <html>
      <head>
        <title>Amogus</title>
      </head>
      <body>
        <h1>amogus</h1>
        <p>{c.req.path}</p>
      </body>
    </html>
  )
})

export default app
