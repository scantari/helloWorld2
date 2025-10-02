// Change the paragraph text
function changeText() {
    document.getElementById("changeableText").textContent = "Just kidding, it is the Good Place!";
}

// Greet the user using the form
document.getElementById("greetingForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevents form from reloading the page
    const name = document.getElementById("nameInput").value;
    document.getElementById("greetingMessage").textContent = `Hello, ${name}!`;
});

// Add favorite foods using JavaScript loop
const favoriteFoods = ["Popcorn", "Tacos", "McDonalds", "Kale"];
const foodList = document.getElementById("foodList");

favoriteFoods.forEach(function(food) {
    const li = document.createElement("li");
    li.textContent = food;
    foodList.appendChild(li);
});

// Handle checkbox form
document.getElementById("courseForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const selectedCourses = [];
    const checkboxes = document.querySelectorAll('input[name="courses"]:checked');

    checkboxes.forEach(function(box) {
        selectedCourses.push(box.value);
    });

    // Show alert
    if (selectedCourses.length > 0) {
        alert("You have taken: " + selectedCourses.join(", "));
    } else {
        alert("You haven't selected any courses.");
    }
});