

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





// Problem 4
// Write a function to copy all the elements of a list with value less than 10 to a new list and return it.


function extract_less_than_ten(nums) {
    // let new_list = []
    // for (num of nums) {
    //     if (num < 10) {
    //         new_list.push(num)
    //     }
    // }
    // return new_list


    let new_list = []
    for (let i=0; i<nums.length; i++) {
        if (nums[i] < 10) {
            new_list.push(nums[i])
        }
    }
    return new_list
}
// console.log(extract_less_than_ten([2, 8, 12, 18])) // [2, 8]


// for (let i=0, k=0; i<10; ++i) {
//     for (let j=0; j<10; ++j, k++) {
//         console.log(i, j, k)
//     }
// }





// Problem 5
// Write a function to find all common elements between two lists.

function common_elements(nums1, nums2) {
    let output = []
    for (let i=0; i<nums1.length; i++) {
        for (let j=0; j<nums2.length; j++) {
            // if nums1[i] == nums2[i] and nums1[i] not in output:
            if (nums1[i] === nums2[j] && !output.includes(nums1[i])) {
                output.push(nums1[i])
            }
        }
    }
    return output

    // let output = []
    // for (num1 of nums1) {
    //     for (num2 of nums2) {
    //         if (num1 == num2 && !output.includes(num1)) {
    //             output.push(num1)
    //         }
    //     }
    // }
    // return output

}
// console.log(common_elements([1, 2, 2, 3], [2, 3, 4])) // [2, 3]


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

// console.log(find_pair([5, 6, 2, 3], 7)) // [5, 2]





// let nums = [5, 6, 7, 8]
// nums.forEach(function(x) {
//     console.log(x)
// })


// Given a string of letters, find the index of each capital letter and return it

function findCapitalIndices(text) {
    // make text all caps using toUpperCase - CODEWARSCODEWARS
    // loop through the indices of the text
    // compare each character of the original text to the corresponding character of the upper case text
    // if they're equal, add the index to an output array


    // 0123456789...
    // CodEWaRsCodEWaRs
    // CODEWARSCODEWARS

    // let upper = text.toUpperCase()
    // let output = []
    // for (let i=0; i<text.length; i++) {
    //     if (upper[i] === text[i]) {
    //         output.push(i)
    //     }
    // }
    // return output


    // loop over the indices of the string
    // compare each letter to the capital version of the letter
    // if they're equal add the index to the output

    // let output = []
    // for (let i=0; i<text.length; ++i) {
    //     if (text[i] == text[i].toUpperCase()) {
    //         output.push(i)
    //     }
    // }
    // return output

    

    // make an upper case alphabet
    // loop through the indices of the text
    // check if the upper case alphabet includes the character
    // if it does, add the index to the output array

    let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let output = []
    for (let i=0; i<text.length; ++i) {
        if (alphabet.includes(text[i])) {
            output.push(i)
        }
    }
    return output



}
//                              0123456789
console.log(findCapitalIndices('CodEWaRsCodEWaRs')) // [0, 3, 4, 6, 8, ...]