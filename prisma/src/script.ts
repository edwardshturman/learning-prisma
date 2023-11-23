import { PrismaClient, User } from '@prisma/client'
const prisma = new PrismaClient()

async function createUser (email: string) {
  const user = await prisma.user.create({
    data: {
      email
    }
  })

  return user
}

const edward = await createUser('emshturman@dons.usfca.edu')
console.log(edward)
