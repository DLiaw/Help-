

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
        const data = await response.json()
        dispatch(allReviews(data.reviews))
    }
}

// Reviews reducers

const oldState = { allReviews: {} }
export default function reviewReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_REVIEWS: {
            let review = action.reviews
            review.forEach(e =>
                newState.allReviews[e.id] = e
            )
            return newState
        }
        default: return state
    }
}
