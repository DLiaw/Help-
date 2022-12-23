

const GET_ALL_BUSINESS = '/business/GET_ALL_BUSINESS'
const NEW_BUSINESS = '/business/NEW_BUSINESS'


// Business actions

const allBusiness = business => {
    return {
        type: GET_ALL_BUSINESS,
        business
    }
}

const newBusiness = business => {
    return {
        type: NEW_BUSINESS,
        business
    }
}

// Business thunks

export const getAllBusiness = () => async dispatch => {
    const response = await fetch("/api/businesses")
    if (response.ok) {
        const data = await response.json()
        dispatch(allBusiness(data))
    }
}

export const createNewBusiness = (business) => async dispatch => {
    const response = await fetch("/api/business/new", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(business)
    })
    if (response.ok) {
        const data = await response.json()
        return data
    } else if (response.status < 500) {
        const data = await response.json()
        if (data.errors) return data
    }
}

// Business reducers

const oldState = { allBusiness: {} }
export default function businessReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_BUSINESS: {
            action.allBusiness.forEach(e => {
                newState.businesses[e.id] = e
            })
            return newState
        }
        default:
            return oldState
    }
}
