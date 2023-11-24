import { z } from 'zod'

const UserSchema = z.object({
  username: z.string()
})

const user = {
  username: 'edwardshturman'
}

console.log(UserSchema.parse(user))
