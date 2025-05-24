import { forwardRef } from 'react'
import Link from 'next/link'
import clsx from 'clsx'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  href?: string
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ className, href, children, ...props }, ref) => {
    const Component = href ? Link : 'div'
    const componentProps = href ? { href } : {}

    return (
      <Component
        ref={ref}
        className={clsx(
          'bg-white overflow-hidden shadow rounded-lg',
          'hover:shadow-md transition-shadow duration-200',
          className
        )}
        {...componentProps}
        {...props}
      >
        <div className="px-4 py-5 sm:p-6">{children}</div>
      </Component>
    )
  }
)

Card.displayName = 'Card' 