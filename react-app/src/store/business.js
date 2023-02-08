const GET_ALL_BUSINESS = '/business/GET_ALL_BUSINESS'
const NEW_BUSINESS = '/business/NEW_BUSINESS'
const ONE_BUSINESS = '/business/ONE_BUSINESS'
const CLEANUP_BUSINESS = '/business/CLEAN_BUSINESS'
const ADD_IMAGE = 'business/ADD_IMAGE'
const DELETE_IMAGE = 'business/DELETE_IMAGE'
// Business actions

const allBusiness = business => {
    return {
        type: GET_ALL_BUSINESS,
        "business": business
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

export const cleanupBusiness = () => {
    return {
        type: CLEANUP_BUSINESS
    }
}

export const addImage = (image) => {
    return {
        type: ADD_IMAGE,
        image
    }
}

// Business thunks

export const addBusinessImage = (image) => async dispatch => {
    const response = await fetch("/api/business_images/new", {
        method: 'POST',
        body: image
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(addImage(image))
        return data
    } else if (response.status < 500) {
        const data = await response.json()
        if (data.errors) return data
    }
}

export const getAllBusiness = () => async dispatch => {
    const response = await fetch("/api/business")
    if (response.ok) {
        const data = await response.json()
        dispatch(allBusiness(data.businesses))
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

export const updateBusiness = (business) => async dispatch => {
    const response = await fetch(`/api/business/${business.id}/edit`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
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

export const deleteOldBusiness = (id) => async dispatch => {
    await fetch(`/api/business/${id}`, {
        method: 'DELETE'
    })
}

export const deleteBusinessImage = (id) => async dispatch => {
    await fetch(`/api/business_images/${id}`, {
        method: 'DELETE'
    })
}
// Business reducers

const oldState = { allBusiness: {}, oneBusiness: {} }
export default function businessReducer(state = oldState, action) {
    const newState = { ...state }
    switch (action.type) {
        case GET_ALL_BUSINESS: {
            if (action.business) {
                action.business.forEach(e => {
                    newState.allBusiness[e.id] = e
                })
            }
            return newState
        }
        case ONE_BUSINESS: {
            newState.oneBusiness = action.business
            return newState;
        }
        case CLEANUP_BUSINESS: {
            newState.allBusiness = {}
            newState.oneBusiness = {}
            return newState
        }
        case DELETE_IMAGE: {
            delete newState.oneBusiness.images[action.id]
            return newState
        }
        default:
            return oldState
    }
}
