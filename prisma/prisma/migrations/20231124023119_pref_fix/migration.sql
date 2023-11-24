/*
  Warnings:

  - You are about to drop the column `userId` on the `UserPreferencesSet` table. All the data in the column will be lost.
  - A unique constraint covering the columns `[userPreferenceSetId]` on the table `User` will be added. If there are existing duplicate values, this will fail.
  - The required column `id` was added to the `UserPreferencesSet` table with a prisma-level default value. This is not possible if the table is not empty. Please add this column as optional, then populate it before making it required.

*/
-- DropForeignKey
ALTER TABLE "UserPreferencesSet" DROP CONSTRAINT "UserPreferencesSet_userId_fkey";

-- DropIndex
DROP INDEX "UserPreferencesSet_userId_key";

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "userPreferenceSetId" TEXT;

-- AlterTable
ALTER TABLE "UserPreferencesSet" DROP COLUMN "userId",
ADD COLUMN     "id" TEXT NOT NULL,
ADD CONSTRAINT "UserPreferencesSet_pkey" PRIMARY KEY ("id");

-- CreateIndex
CREATE UNIQUE INDEX "User_userPreferenceSetId_key" ON "User"("userPreferenceSetId");

-- AddForeignKey
ALTER TABLE "User" ADD CONSTRAINT "User_userPreferenceSetId_fkey" FOREIGN KEY ("userPreferenceSetId") REFERENCES "UserPreferencesSet"("id") ON DELETE SET NULL ON UPDATE CASCADE;
