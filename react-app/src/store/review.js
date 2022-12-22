

const GET_ALL_REVIEWS = '/review/GET_ALL_REVIEWS'



// Review actions

const allReviews = reviews => {
    return {
        type: GET_ALL_REVIEWS,
        reviews
    }
}

// Reviews thunks

export const getAllReviews = () => async dispatch => {
    const response = await fetch("/api/reviews")
    if (response.ok) {
        const reviews = await response.json()
        console.log(reviews, 'FROM THUNK')
        dispatch(allReviews(reviews.reviews))
    }
}

// Reviews reducers

const oldState = { allReviews: {} }
export default function reviewReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_REVIEWS: {
            let review = action.reviews
            console.log(review, 'COMING FROM REDUCER')
            review.forEach(e =>
                newState.allReviews[e.id] = e
            )
            return newState
        }
        default: return state
    }
}
