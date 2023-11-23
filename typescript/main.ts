// Inferred types
const x = 10
const y = 20
/* x = 'hello' // Error because x is inferred to be a number */

// Explicit types
const valid: boolean = true
const total: number = 0
const person: string = 'Edward'

const greeting: string = `Hello, ${person}!`
console.log(greeting)

// Arrays
const list1: number[] = [1, 2, 3] // C-like syntax
const list2: Array<number> = [1, 2, 3] // Java-like syntax

// Tuples
const person1: [string, number] = ['Chris', 22]

// Enums
enum Color {
    Red,
    Green,
    Blue
}

const color: Color = Color.Green

// Any
let randomValue: any = 10
randomValue = true
randomValue = 'Edward'
// No error because randomValue is of type any

// Unknown
let myVariable: unknown = 10
myVariable = true
myVariable = 'Edward'
;(myVariable as string).toUpperCase()

// Union types
let multiType: number | boolean
multiType = 20
multiType = true

// Functions
function add(num1: number, num2: number): number {
    return num1 + num2
}

let result = add(5, 10)
console.log(result)

// Optional parameters
function add2(num1: number, num2?: number): number {
    if (num2) return num1 + num2
    else return num1
}

result = add2(5)
console.log(result)

// Default parameters
function add3(num1: number, num2: number = 10): number {
    return num1 + num2
}

result = add3(5)
console.log(result) // 15
result = add3(5, 20)
console.log(result) // 25

// Interfaces
interface Person {
    firstName: string
    lastName?: string
}

function fullName(person: Person) {
    console.log(`${person.firstName} ${person.lastName || ''}`)
}

const newPerson = {
    firstName: 'Imposter',
    lastName: 'from Among Us'
}

fullName(newPerson)

// Classes
class Employee {
    name: string

    constructor(name: string) {
        this.name = name
    }

    greet() {
        console.log(`Good morning ${this.name}`)
    }
}

const employee = new Employee('Sam')
console.log(employee.name)
employee.greet()

// Inheritance
class Manager extends Employee {
    constructor(managerName: string) {
        super(managerName)
    }

    delegateWork() {
        console.log(`Delegating tasks....`)
    }
}

const manager = new Manager('Edward')
manager.delegateWork()
manager.greet()
console.log(manager.name)
