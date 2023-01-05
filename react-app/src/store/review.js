const GET_ALL_REVIEWS = '/review/GET_ALL_REVIEWS'
const ONE_REVIEW = '/review/ONE_REVIEW'
const CLEANUP_REVIEW = '/review/CLEANUP_REVIEW'
// Review actions

const allReviews = reviews => {
    return {
        type: GET_ALL_REVIEWS,
        reviews
    }
}

const oneReview = reviews => {
    return {
        type: ONE_REVIEW,
        reviews
    }
}

export const cleaupReview = () => {
    return {
        type: CLEANUP_REVIEW
    }
}
// Reviews thunks

export const newReview = (data) => async dispatch => {
    const response = await fetch(`/api/business/${data.business_id}/reviews`, {
        method: "POST",
        headers: {
            "content-Type": 'application/json'
        },
        body: JSON.stringify(data)
    })
    if (response.ok) {
        const data = await response.json();
        return data
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data
    }
}

export const getAllReviews = () => async dispatch => {
    const response = await fetch("/api/reviews")
    if (response.ok) {
        const data = await response.json()
        dispatch(allReviews(data.reviews))
    }
}

export const getOneReview = (id) => async dispatch => {
    const response = await fetch(`/api/reviews/${id}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(oneReview(data.review))
    }
}

export const deleteOldReview = (id) => async dispatch => {
    await fetch(`/api/reviews/${id}`, {
        method: 'DELETE'
    })
}

export const updateReview = (review) => async dispatch => {
    const response = await fetch(`/api/reviews/${review.review_id}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(review)
    })

    if (response.ok) {
        const data = await response.json()
        return data
    } else if (response.status < 500) {
        const data = await response.json()
        if (data.errors) return data
    }
}


// Reviews reducers

const oldState = { allReviews: {}, oneReview: {} }
export default function reviewReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_REVIEWS: {
            let data = action.reviews
            data.forEach(e =>
                newState.allReviews[e.id] = e
            )
            return newState
        }
        case ONE_REVIEW: {
            newState.oneReview = action.reviews
            return newState
        }
        case CLEANUP_REVIEW: {
            newState.allReviews = {}
            newState.oneReview = {}
            return newState
        }
        default:
            return state
    }
}
