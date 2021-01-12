

// Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

function is_even(x) {
    if (x % 2 === 1) {
        return false
    } else {
        return true
    }
    // return x%2 === 0
}
// console.log(is_even(5)) // false
// console.log(is_even(6)) // true




// Strings - Problem 1
// Get a string from the user, print out another string, doubling every letter.

function double_letters(word) {
    // loop over the word
    // every iteration, double it
    var output = ''
    for (char of word) {
        // output += char.repeat(2)
        output += char + char
    }
    return output
}
// console.log(double_letters('hello')) // hheelllloooo


// Problem 2
// Return the number of letter occurances in a string.

function count_letter(letter, word) {
    let count = 0
    for (char of word) {
        if (char === letter) {
            count++
        }
    }
    return count
}
// console.log(count_letter('i', 'antidisestablishmentterianism')) // 5
// console.log(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) // 2




// Problem 3
// Return the letter that appears the latest in the english alphabet.

function latest_letter(word) {

    // let biggest = 0
    // for (let i=0; i<word.length; ++i) {
    //     if (word.charCodeAt(i) > biggest) {
    //         biggest = word.charCodeAt(i)
    //     }
    // }
    // return biggest

    // let chars = []
    // for (let i=0; i<word.length; ++i) {
    //     chars.push(word[i])
    // }
    // chars.sort()
    // return chars[chars.length - 1]


    let biggest = 0
    for (char of word) {
        if (char.charCodeAt(0) > biggest) {
            biggest = char.charCodeAt(0)
        }
    }
    return String.fromCharCode(biggest)
}
// console.log(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) // v



// Problem 5
// Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

function snake_case(text) {
    let alphabet = 'abcdefghijklmnopqrstuvwxyz_'
    text = text.toLowerCase()
    text = text.replaceAll(' ', '_')
    // iterate over and see if the char is in that string
    let output = ''
    for (char of text) {
        // if char in alphabet
        if (alphabet.includes(char)) {
            output += char
        }
    }
    return output

}
// console.log(snake_case('Hello World!')) // hello_world
// console.log(snake_case('This is another example.')) // this_is_another_example



// Problem 2
// Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

function eveneven(nums) {
    let output = []
    for (num of nums) {
        if (num%2 == 0) {
            output.push(num)
        }
    }
    if (output.length%2 == 0) {
        return true
    } else {
        return false
    }

    // let counter = 0
    // for (let i=0; i<nums.length; ++i) {
    //     if (nums[i]%2 == 0) {
    //         counter += 1
    //     }
    // }
    // return counter%2 == 0
}

// console.log(eveneven([5, 6, 2])) // True
// console.log(eveneven([5, 5, 2])) // False



// Problem 7
// Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.



// def find_pair(nums, target):
//     for i in range(len(nums)):
//         for j in range(i+1, len(nums)):
//             if nums[i] + nums[j] == target:
//                 return [nums[i], nums[j]]
//     return None


function find_pair(nums, target) {
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            // console.log(i + ' ' + j)
            if (nums[i] + nums[j] == target) {
                return [nums[i], nums[j]]
            }
        }
    }
    return null
}

console.log(find_pair([5, 6, 2, 3], 7)) // [5, 2]