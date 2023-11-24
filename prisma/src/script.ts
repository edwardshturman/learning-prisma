import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()

async function createUser (email: string) {
  const user = await prisma.user.create({
    data: {
      email
    }
  })

  return user
}

async function deleteUsers () {
  const users = await prisma.user.deleteMany()
  return users
}

const edward = await createUser('emshturman@dons.usfca.edu')
console.log(edward)

const deletedUsers = await deleteUsers()
console.log(deletedUsers)
