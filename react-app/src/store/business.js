

// const GET_ALL_BUSINESS = '/business/GET_ALL_BUSINESS'



// // Business actions

// const allBusiness = business => {
//     return {
//         type: GET_ALL_BUSINESS,
//         business
//     }
// }

// // Business thunks

// export const getAllBusiness = () => async dispatch => {
//     const response = await fetch("/api/businesses")
//     if (response.ok) {
//         const business = await response.json()
//         dispatch(allBusiness(business))
//     }
// }

// // Business reducers

// const oldState = { allBusiness: {} }
// export default function businessReducer(state = oldState, action) {
//     const newState = { ...state }
//     switch (action.type) {
//         case GET_ALL_BUSINESS: {
//             action.allBusiness.forEach(e => {
//                 newState.businesses[e.id] = e
//             })
//             return newState
//         }
//     }
// }
