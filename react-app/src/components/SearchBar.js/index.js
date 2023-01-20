import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getAllBusiness } from '../../store/business'
import { NavLink } from 'react-router-dom'
import './searchbar.css'

const SearchBar = () => {
    const dispatch = useDispatch()
    const [filterData, setFilterData] = useState([])
    const business = useSelector(state => {
        return Object.values(state.business.allBusiness)
    })

    useEffect(() => {
        if (!business.length) dispatch(getAllBusiness())
    }, [dispatch])

    const handleFilter = (e) => {
        const search = e.target.value
        const filter = business.filter((value) => {
            return value.name.toLowerCase().includes(search.toLowerCase())
        })
        if (search === '') setFilterData([])
        else setFilterData(filter)
    }

    if (!business) return null
    return (
        <div className='searchbar'>
            <div className='searchInput'>
                <input type='text'
                    className='searchTextInput'
                    onChange={handleFilter}
                    placeholder='Businesses...' />
                <div className='searchIcon'><i class="fa-solid fa-magnifying-glass" /></div>
            </div>
            {filterData.length != 0 && (
                < div className='searchResults'>
                    {filterData.map((value, i) => {
                        return <NavLink style={{ textDecoration: 'none', color: 'grey' }} key={i} to={`/business/${value.id}`}>{value.name}</NavLink>
                    })}
                </div>
            )}
        </div >
    )
}

export default SearchBar;
