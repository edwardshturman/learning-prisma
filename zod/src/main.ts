import { z } from 'zod'

const themes = ['LIGHT', 'DARK'] as const

const UserSchema = z.object({
  username: z.string().min(3).max(20),
  age: z.number().gt(0).optional(),
  email: z.string().email(),
  isAdmin: z.boolean().default(false),
  theme: z.enum(themes).default('DARK')
})

type User = z.infer<typeof UserSchema>

const user: User = {
  username: 'edwardshturman',
  age: 20,
  email: 'emshturman@dons.usfca.edu',
  isAdmin: true,
  theme: 'DARK'
}

console.log(UserSchema.parse(user))
