// async function fetchAlcoholStressed() {
//   // get data from server
//   let res = await fetch("/api/insights")

//   // convert list of JSON to objects
//   let alcoholStressed = await res.json()

//   console.log(alcoholStressed) // debug log
// }

// async function fetchAlcoholNotStressed() {
//   // get data from server
//   let res = await fetch("/api/insights")

//   // convert list of JSON to objects
//   let alcoholNotStressed = await res.json()

//   console.log(alcoholNotStressed) // debug log
// }

// async function fetchSpecialization() {
//   // get data from server
//   let res = await fetch("/api/insights")

//   // convert list of JSON to objects
//   let specialization = await res.json()

//   console.log(specialization) // debug log
// }
$(".predict-btn").on("click", async function () {
  let ageValue = $('input[name="age"]:checked').val()
  let genderValue = $('input[name="gender"]:checked').val()
  let specializationValue = $('input[name="specialization"]:checked').val()
  let workHourValue = $('input[name="workHour"]:checked').val()
  let patientsPerDayValue = $('input[name="patientsPerDay"]:checked').val()
  let overtimeWorkInterestValue = $(
    'input[name="overtimeWorkInterest"]:checked'
  ).val()
  let overtimeWorkPaidValue = $('input[name="overtimeWorkPaid"]:checked').val()
  let sectorValue = $('input[name="sector"]:checked').val()

  let predictValues = {
    age: ageValue,
    gender: genderValue,
    workHours: workHourValue,
    Specialization: specializationValue,
    patientPerDay: patientsPerDayValue,
    overtimeWorkInterest: overtimeWorkInterestValue,
    overtimeWorkPaid: overtimeWorkPaidValue,
    sector: sectorValue,
  }

  const res = await fetch("/api/predict", {
    method: "POST",
    contentType: "application/json",
    body: JSON.stringify(predictValues),
  })

  let prediction = await res.json()
  if (prediction.status === "error") {
    $(".text")
      .html(
        `
      ${prediction.massage}
    `
      )
      .fadeIn("slow")
    setTimeout(function () {
      $(".text").fadeOut("slow")
    }, 5000)
  }

  if (prediction.massage.col11_predict === 1)
    $(".predictionInfo").html(`
      <p style="color: #6351CE" class="special_tag">Employee at risk for some stress 😒</p>
    `)
  else if (prediction.massage.col11_predict === 2)
    $(".predictionInfo").html(`
      <p style="color: #FF595E" class="special_tag">Employee at high risk for stress 🤦‍♂️🤦‍♀️</p> 
    `)
  else if (prediction.massage.col11_predict === 3)
    $(".predictionInfo").html(`
        <p style="color: #00A35C" class="special_tag">Employee at low risk for stress 😁👍</p> 
      `)
})
