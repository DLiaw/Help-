

const GET_ALL_BUSINESS = '/business/GET_ALL_BUSINESS'
const NEW_BUSINESS = '/business/NEW_BUSINESS'
const ONE_BUSINESS = '/business/ONE_BUSINESS'

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

const oneBusiness = business => {
    return {
        type: ONE_BUSINESS,
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
        dispatch(newBusiness(data))
        return data
    } else if (response.status < 500) {
        const data = await response.json()
        if (data.errors) return data
    }
}

export const getOneBusiness = (business) => async dispatch => {

    const response = await fetch(`/api/business/${business}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(oneBusiness(data))
    }
}

// Business reducers

const oldState = { allBusiness: {}, oneBusiness: {} }
export default function businessReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_BUSINESS: {
            action.allBusiness.forEach(e => {
                newState.businesses[e.id] = e
            })
            return newState
        }
        case ONE_BUSINESS: {
            newState.oneBusiness = action.business
            return newState;
        }
        default:
            return oldState
    }
}
